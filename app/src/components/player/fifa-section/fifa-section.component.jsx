import React from 'react';

import { Radar } from 'react-chartjs-2';
import Skeleton from 'react-loading-skeleton';

import './fifa-section.styles.scss';


function loadChartData(playerData) {

    return {
        labels: ['Pace', 'Shooting', 'Passing', 'Dribbling', 'Defending', 'Physical'],
        datasets: [{
            label: playerData.short_name, 
            backgroundColor: 'rgb(61, 61, 92, 0.1)',
            borderColor: 'rgb(61, 61, 92)',
            data: [playerData.pace, playerData.shooting, playerData.passing, playerData.dribbling, playerData.defending, playerData.physic]
        },
        {
            label: "Average Pro Player",
            backgroundColor: 'rgb(99, 132, 255, 0.1)',
            borderColor: 'rgb(99, 132, 255)',
            data: [67.7, 52.3, 57.2, 62.5, 51.6, 64.9]
        }
        ]
    }
}

const FifaSection = ({playerData}) => (
    <>
        <div className='fifaSection'>
            <h2>FIFA Ratings</h2>
            <div className='ratingsBlock'>
                <span className='overallRating'>
                    {playerData ? playerData.overall : 'loading' }
                </span>
                
                <span className='potentialRating'>
                    {playerData ? playerData.potential : 'loading' }
                </span>
            </div>
            {playerData ?
            <> 
                <Radar data={loadChartData(playerData)} />
                <b>Similar Players</b>
                <ul>
                    {playerData.transfermarkt.similar_players.map((player) =>
                            <li>
                                <a>{player}</a>
                            </li>
                        )}
                </ul>
            </>
            : 
            <Skeleton /> }
        </div>
    </>
);

export default FifaSection;