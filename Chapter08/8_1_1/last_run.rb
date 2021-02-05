  def self.log_last_run
    fileName = "poll_all.date"
    aFile = File.new(::Rails.root.to_s + "/log/" + fileName, "w")
    contents = Time.now.to_i.to_s
    $stderr.puts "Writing '%s' with '%s'" % [aFile.path, contents]
    aFile.write(contents)
    aFile.close
  end
