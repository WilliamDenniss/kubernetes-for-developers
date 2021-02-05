YourApp::Application.routes.draw do
  # Health checks
  get "/healthz" => "probez#healthz"
  get '/readyz', :to => 'probez#readyz'
end