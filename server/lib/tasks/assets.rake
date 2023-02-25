namespace :assets do
  desc 'Provide deployment pipeline with a rake task to run that does nothing.'
  task :precompile do
    puts 'Not precompiling assets...'
  end
end