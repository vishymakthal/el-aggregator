import React from 'react';
import './depthchartslot.styles.scss';

import DepthChartPlayer from '../depthchartplayer/depthchartplayer.component';

const DepthChartSlot = ({players}) => (
    <div className="depthChartSlot">
        <table>
            {players.reverse().map(p => (<DepthChartPlayer player={p}/>))}
        </table>
    </div>
);

export default DepthChartSlot;