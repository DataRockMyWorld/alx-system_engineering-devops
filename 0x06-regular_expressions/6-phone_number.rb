#!/usr/bin/env ruby
# A regular expression matching a 10 digit phone number
puts ARGV[0].scan(/\d{10}/).join