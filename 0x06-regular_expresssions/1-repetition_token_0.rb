#!/usr/bin/env ruby
#Matches the pattern hbt{2,5}n
puts ARGV[0].scan(/hbt{2,5}n/).join
