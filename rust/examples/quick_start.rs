use crawlora_googleplay::{
    Client, GoogleplaySearchParams, ModelGoogleplaySearchResultsResponseDoc,
};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api_key = std::env::var("CRAWLORA_API_KEY")?;
    let client = Client::new(api_key)?;
    let response = client
        .googleplay
        .search(GoogleplaySearchParams {
            term: Some("podcast player".to_owned()),
            ..Default::default()
        })
        .await?;
    let data: ModelGoogleplaySearchResultsResponseDoc = response.into_json()?;
    println!("{data:#?}");
    Ok(())
}
