Rails.application.routes.draw do
  resources :artists do
    get '/show' => 'artists#show'
  end

  root 'welcome#index'
end