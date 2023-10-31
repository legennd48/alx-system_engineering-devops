#!/usr/bin/env ruby
# Module: 8. Textme

puts ARGV[0].scan(/\[(?:from:|to:|flags:)(.*?)\]/).join(",")
