import React from 'react';

import './autocomplete.styles.scss';

function AutoComplete({ hits, currentRefinement, refine, indexName }) {
  
  if (indexName === "players") {
    return (
      <div className='autoComplete'>  
        <input
              type="search"
              value={currentRefinement}
              placeholder="Search for a player"
              onChange={event => refine(event.currentTarget.value)}
            />
        <div className='searchResults'>      
          {hits.map(hit => (
            <div className='searchResult'>
              <img alt={hit.short_name} src={`https://el-aggregator-api-q3hl2qd3ia-uk.a.run.app/api/v1/images/${hit.sofifa_id}?q=player`}/>
              <a key={hit.sofifa_id} href={`/player/${hit.sofifa_id}`}>{hit.short_name}</a>
            </div>
          ))}
        </div>
      </div>
    )
  } else {
    return(
      <div className='autoComplete'>  
        <input
              type="search"
              value={currentRefinement}
              placeholder="Search for a team"
              onChange={event => refine(event.currentTarget.value)}
            />
        <div className='searchResults'>      
          {hits.map(hit => (
            <div className='searchResult'>
              <img alt={hit.name} src={`https://el-aggregator-api-q3hl2qd3ia-uk.a.run.app/api/v1/images/${hit.ext}?q=team`}/>
              <a key={hit.ext} href={`/team/${hit.ext}/${hit.name}`}>{hit.name}</a>
            </div>
          ))}
        </div>
      </div>
    )
  }

  
};

export default AutoComplete;