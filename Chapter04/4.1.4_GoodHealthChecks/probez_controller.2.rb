# encoding: UTF-8
class ProbezController < ApplicationController
  @@last_readyz = Time.now

  def readyz
    begin
      connection = ActiveRecord::Base.connection
      result = connection.execute("SELECT id FROM users LIMIT 1;")
      @@last_readyz = Time.now
      render text: 'Ready', status: 200
    rescue Mysql2::Error
      logger.debug "readyz: " + $!.inspect
      render text: 'Not Ready', status: 503
    end
  end

  def healthz
    if (Time.now > @@last_readyz + 5.minutes)
      render text: 'Not Healthy', status: 503
    else
      render text: 'OK', status: 200
    end
  end
end
