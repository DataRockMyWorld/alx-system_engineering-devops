#!/usr/bin/env ruby
# A regular expression matching variations of hbtn
puts ARGV[0].scan(/hbt{1,4}n/).join