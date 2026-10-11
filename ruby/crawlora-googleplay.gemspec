require_relative "lib/crawlora/googleplay/version"

Gem::Specification.new do |spec|
  spec.name = "crawlora-googleplay"
  spec.version = Crawlora::Googleplay::VERSION
  spec.summary = "Google Play API client for Crawlora (11 endpoints)"
  spec.description = "Ruby client for Crawlora's hosted Google Play API. Covers app search, details, reviews, ratings, permissions, data safety, charts, similar apps, and developers across 11 endpoints."
  spec.authors = ["Crawlora"]
  spec.license = "MIT"
  spec.required_ruby_version = ">= 2.6"
  spec.files = Dir["lib/**/*.rb", "README.md", "CHANGELOG.md", "LICENSE"]
  spec.require_paths = ["lib"]
  spec.homepage = "https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=googleplay-ruby-homepage"
  spec.metadata = { "source_code_uri" => "https://github.com/Crawlora-org/crawlora-googleplay", "documentation_uri" => "https://github.com/Crawlora-org/crawlora-googleplay/blob/main/ruby/README.md", "rubygems_mfa_required" => "true" }

end
