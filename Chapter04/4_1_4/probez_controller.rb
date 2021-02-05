# encoding: UTF-8
class ProbezController < ApplicationController

  def readyz
    begin
      connection = ActiveRecord::Base.connection
      result = connection.execute("SELECT id FROM users LIMIT 1;")
      render text: 'Ready', status: 200
    rescue Mysql2::Error
      logger.debug "readyz: " + $!.inspect
      render text: 'Not Ready', status: 503
    end
  end

  def healthz
    render text: 'OK', status: 200
  end
end
