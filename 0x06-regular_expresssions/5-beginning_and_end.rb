#!/usr/bin/env ruby
#Matches string that starts with h, ends with n,
#with any single character in between
puts ARGV[0].scan(/^h.n$/).join
