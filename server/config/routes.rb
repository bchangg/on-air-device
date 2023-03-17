Rails.application.routes.draw do
  # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html

  # Defines the root path route ("/")
  root "home#hello"

  namespace :api do
    namespace 'v1' do
      scope 'mqtt' do
        post 'publish', to: 'mqtt#publish'
      end
    end
  end
end
