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
           </br>
            <a class="button" href=/team?id={{ext}}&name={{name}}>{{name}}</a>
          </div>
        </br>
      `,
    },
  })
);
const playerSearch = instantsearch({
  indexName: 'players',
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
            <a class="button"  href=/player?id={{sofifa_id}}>{{short_name}}</a>
          </div>
          </br>
      `,
    },
  })
);

teamSearch.start()
playerSearch.start()