import React from 'react';
import ReactPlayer from 'react-player/youtube'

import './highlight-section.styles.scss';



function HighlightSection({playerData, youtubePreview}) {
    
    const goals = playerData.reddit.goals.map((goal) =>
                    <div className='highlightLink'>
                        <a href={`${goal.link}`} target="blank">{goal.title}</a>
                    </div>
                 );    
    return (
        <>
            <div className='highlightSection'>

                <div className='highlightSubsection'>               
                    <h3> YOUTUBE HIGHLIGHTS </h3> 
                        <ReactPlayer url={`https://youtube.com/watch?v=${youtubePreview.video_id}`} width={'70%'}/>
                </div>

                <div className='highlightSubsection'>               
                    <h3> /r/soccer HIGHLIGHTS </h3>
                      <ul>
                        {goals}
                      </ul>
                </div>                
                
            </div>
        </>
    )
}

export default HighlightSection;
