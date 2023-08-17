# Galois field arithmetic operations
def gf_add(a, b, p)
  (a + b) % p
end

def gf_sub(a, b, p)
  (a - b + p) % p
end

def gf_mul(a, b, p)
  (a * b) % p
end

def gf_inv(a, p)
  raise 'Inverse does not exist' if a == 0
  (1..p-1).find { |i| (i * a) % p == 1 } || raise('Inverse not found')
end

def gf_div(a, b, p)
  gf_mul(a, gf_inv(b, p), p)
end

def interpolate(d, x, y, p)
  coeff = Array.new(d, 0)

  for i in 0...d
    product = 1
    t = Array.new(d, 0)

    for j in 0...d
      next if i == j
      product = gf_mul(product, gf_sub(x[i], x[j], p), p)
    end

    product = gf_div(y[i], product, p)
    t[0] = product

    for j in 0...d
      next if i == j
      (d - 1).downto(1) do |k|
        t[k] = gf_add(t[k], t[k - 1], p)
        t[k - 1] = gf_mul(t[k - 1], gf_sub(0, x[j], p), p)
      end
    end

    for j in 0...d
      coeff[j] = gf_add(coeff[j], t[j], p)
    end
  end

  coeff
end

def main
  if ARGV.length != 2
    puts "Error: Please provide a prime number and a file path."
  else
    p = ARGV[0].to_i
    path = ARGV[1]
    
    unless File.exist?(path)
      puts "Error: The file at '#{path}' doesn't exist!"
      return
    end

    begin
      d = 0
      x = []
      y = []

      File.open(path, 'r') do |file|
        file.each_line do |line|
          split = line.split(" ")
          raise ValueError if split.length != 2
          x << split[0].to_i
          y << split[1].to_i
          d += 1
        end
      end

      coeff = interpolate(d, x, y, p)
      puts coeff.join(" ")
    rescue
      puts "Error: Invalid input format"
    end
  end
end

main
