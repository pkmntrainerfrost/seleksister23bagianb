program InterpolationProgram
  implicit none
  integer :: d, i, n
  real(8), allocatable :: x(:), y(:), p(:)
  character(len=200) :: path

  if (command_argument_count() < 1) then
      print *, "Error: Please provide a file path."
      stop
  end if    

  call get_command_argument(1, path)
  open(unit=10, file=trim(path), status="old", action="read", iostat=n)

  if (n /= 0) then
      print *, "Error: The file at '", trim(path), "' doesn't exist!"
      stop
  end if

  d = 0
  do
      read(10, *, iostat=n) 
      if (n /= 0) exit
      d = d + 1
  end do

  rewind(10)
  allocate(x(d), y(d))

  do i = 1, d
      read(10, *) x(i), y(i)
  end do

  close(10)

  p = interpolate(d, x, y)

  do i = 1, d
    write(*, '(f0.16, 1x)', advance='no') p(i)
  end do

contains

  function interpolate(d, x, y) result(p)
      integer, intent(in) :: d
      real(8), intent(in) :: x(d), y(d)
      real(8) :: p(d)
      integer :: i, j, k
      real(8) :: product
      real(8), dimension(d) :: t

      p = 0.0

      do i = 1, d
          product = 1.0
          t = 0.0

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
      end do
  end function interpolate

end program InterpolationProgram
