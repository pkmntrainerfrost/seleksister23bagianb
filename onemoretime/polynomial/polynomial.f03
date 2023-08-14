program InterpolationProgram

  implicit none
  integer :: d, i
  real(8), allocatable :: x(:), y(:), p(:)
  character(100) :: path

  if (command_argument_count() < 1) then
      print *, "Error: Please provide a file path."
      stop
  end if

  call get_command_argument(1, path)
  call read_data(trim(path), d, x, y)
  call interpolate(d, x, y, p)

  do i = 1, d
      print *, p(i), " "
  end do

contains

  subroutine read_data(filename, d, x, y)
      implicit none
      character(len=*), intent(in) :: filename
      integer, intent(out) :: d
      real(8), allocatable, intent(out) :: x(:), y(:)
      real(8) :: x_val, y_val
      integer :: iounit
      d = 0

      open(newunit=iounit, file=filename, status='old', action='read')

      do
          read(iounit, *, iostat=d) x_val, y_val
          if (d /= 0) exit
          d = d + 1
      end do
      rewind(iounit)

      allocate(x(d), y(d))

      do d = 1, d
          read(iounit, *) x(d), y(d)
      end do

      close(iounit)
  end subroutine read_data

  subroutine interpolate(d, x, y, p)
      implicit none
      integer, intent(in) :: d
      real(8), intent(in) :: x(d), y(d)
      real(8), allocatable, intent(out) :: p(:)
      real(8) :: product
      real(8), allocatable :: t(:)
      integer :: i, j, k

      allocate(p(d))
      p = 0.0d0

      do i = 1, d
          product = 1.0d0
          allocate(t(d))
          t = 0.0d0
          do j = 1, d
              if (i /= j) then
                  product = product * (x(i) - x(j))
              end if
          end do
          product = y(i) / product
          t(1) = product

          do j = 1, d
              if (i /= j) then
                  do k = d, 2, -1
                      t(k) = t(k) + t(k - 1)
                      t(k - 1) = t(k - 1) * (-x(j))
                  end do
              end if
          end do

          do j = 1, d
              p(j) = p(j) + t(j)
          end do
          deallocate(t)
      end do
  end subroutine interpolate

end program InterpolationProgram
