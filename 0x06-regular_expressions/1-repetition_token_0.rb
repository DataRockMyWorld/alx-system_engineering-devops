#!/usr/bin/env ruby
# A regular expression matching variations of hbttn
puts ARGV[0].scan(/hbt{2,5}n/).join