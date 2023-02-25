class HomeController < ApplicationController
  def hello
    render plain: 'Welcome to the On-Air-Device API'
  end
end