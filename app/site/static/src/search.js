const teamSearch = instantsearch({
  indexName: 'teams',
  searchClient: algoliasearch('W7AILP8P97', 'b927f0834171ab885b9d31df62a115de'),
  routing: true,
  hitsPerPage: 5
});

teamSearch.addWidget(
  instantsearch.widgets.searchBox({
    container: '#teamSearchbox',
    showReset: false,
    showSubmit: false
  })
);

teamSearch.addWidget(
  instantsearch.widgets.hits({
    container: '#teamHits',
    templates: {
      item: `
          <div class="container">
           <a href=/team?id={{objectID}}><img src="{{img}}"></img></a>
           </br>
            <a class="button" href=/team?id={{objectID}}>{{name}}</a>
          </div>
        </br>
      `,
    },
  })
);
const playerSearch = instantsearch({
  indexName: 'dev_players',
  searchClient: algoliasearch('W7AILP8P97', 'b927f0834171ab885b9d31df62a115de'),
  routing: true,
  hitsPerPage: 5
});

playerSearch.addWidget(
  instantsearch.widgets.searchBox({
    container: '#playerSearchbox',
    showReset: false,
    showSubmit: false
  })
);

playerSearch.addWidget(
  instantsearch.widgets.hits({
    container: '#playerHits',
    templates: {
      item: `
            <div class="container"> 
          <div class="container">
            <div class="container"> 
           <img src="https://cdn.sofifa.org/players/10/20/{{sofifa_id}}.png" ></img>
           </br>
            <a class="button"  href=/player?id={{objectID}}>{{short_name}}</a>
          </div>
          </a>
          </br>
      `,
    },
  })
);

teamSearch.start()
playerSearch.start()