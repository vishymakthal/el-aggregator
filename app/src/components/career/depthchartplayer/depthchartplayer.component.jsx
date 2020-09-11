import React from 'react';
import './depthchartplayer.styles.scss';

const DepthChartPlayer = (props) => (
    <div className="depthChartPlayer">
        <div className="playerRow">
            <div>{props.player.short_name} | {props.player.position} |{props.player.age} </div>
            <div className="playerOverall">{props.player.overall}</div>
        </div>
    </div>
)

export default DepthChartPlayer;