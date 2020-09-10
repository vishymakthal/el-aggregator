import React from 'react';
import './depthchartrow.styles.scss';
import DepthChartSlot from '../depthchartslot/depthchartslot.component';

class DepthChartRow extends React.Component {
    render()
    {
        const slots = []
        // const squad = [{"age":24,"attacking_crossing":76,"attacking_finishing":52,"attacking_heading_accuracy":60,"attacking_short_passing":76,"attacking_volleys":41,"body_type":"Lean","cam":"71+3","cb":"73+3","cdm":"74+3","cf":"70+3","club":"Arsenal","cm":"70+3","contract_valid_until":2023.0,"defending":76.0,"defending_marking":75,"defending_sliding_tackle":80,"defending_standing_tackle":78,"dob":"1995-03-19","dribbling":78.0,"goalkeeping_diving":8,"goalkeeping_handling":14,"goalkeeping_kicking":14,"goalkeeping_positioning":13,"goalkeeping_reflexes":12,"height_cm":178,"international_reputation":3,"joined":"2014-07-01","lam":"71+3","lb":"78+3","lcb":"73+3","lcm":"70+3","ldm":"74+3","lf":"70+3","lm":"74+3","long_name":"H\u00e9ctor Beller\u00edn Moruno","ls":"65+3","lw":"73+3","lwb":"78+3","mentality_aggression":72,"mentality_composure":70,"mentality_interceptions":78,"mentality_penalties":62,"mentality_positioning":67,"mentality_vision":66,"movement_acceleration":94,"movement_agility":79,"movement_balance":77,"movement_reactions":78,"movement_sprint_speed":90,"nationality":"Spain","overall":80,"pace":92.0,"passing":70.0,"physic":66.0,"player_positions":"RB, RWB","player_tags":"#Speedster","player_traits":"Early Crosser","player_url":"https://sofifa.com/player/203747/hector-bellerin-moruno/20/159586","potential":85,"power_jumping":64,"power_long_shots":43,"power_shot_power":52,"power_stamina":77,"power_strength":58,"preferred_foot":"Right","ram":"71+3","rb":"78+3","rcb":"73+3","rcm":"70+3","rdm":"74+3","real_face":"Yes","release_clause_eur":34600000.0,"rf":"70+3","rm":"74+3","rs":"65+3","rw":"73+3","rwb":"78+3","shooting":51.0,"short_name":"H\u00e9ctor Beller\u00edn","skill_ball_control":78,"skill_curve":63,"skill_dribbling":77,"skill_fk_accuracy":50,"skill_long_passing":59,"skill_moves":3,"st":"65+3","team_jersey_number":2.0,"team_position":"SUB","value_eur":17500000,"value_gbp":"\u00a328.80m","wage_eur":69000,"weak_foot":3,"weight_kg":74,"work_rate":"High/Low"}, {"age":24,"attacking_crossing":59,"attacking_finishing":46,"attacking_heading_accuracy":68,"attacking_short_passing":74,"attacking_volleys":45,"body_type":"Normal","cam":"64+2","cb":"74+2","cdm":"73+2","cf":"62+2","club":"Arsenal","cm":"68+2","contract_valid_until":2022.0,"defending":74.0,"defending_marking":72,"defending_sliding_tackle":74,"defending_standing_tackle":77,"dob":"1995-01-20","dribbling":68.0,"goalkeeping_diving":11,"goalkeeping_handling":14,"goalkeeping_kicking":12,"goalkeeping_positioning":7,"goalkeeping_reflexes":12,"height_cm":183,"international_reputation":1,"joined":"2014-07-28","lam":"64+2","lb":"71+2","lcb":"74+2","lcm":"68+2","ldm":"73+2","lf":"62+2","lm":"64+2","long_name":"Calum Chambers","ls":"60+2","lw":"62+2","lwb":"70+2","mentality_aggression":83,"mentality_composure":64,"mentality_interceptions":74,"mentality_penalties":54,"mentality_positioning":50,"mentality_vision":60,"movement_acceleration":59,"movement_agility":60,"movement_balance":66,"movement_reactions":73,"movement_sprint_speed":66,"nationality":"England","overall":75,"pace":63.0,"passing":65.0,"physic":76.0,"player_positions":"CDM, CM, CB","player_traits":"Injury Prone","player_url":"https://sofifa.com/player/205989/calum-chambers/20/159586","potential":80,"power_jumping":71,"power_long_shots":53,"power_shot_power":52,"power_stamina":72,"power_strength":75,"preferred_foot":"Right","ram":"64+2","rb":"71+2","rcb":"74+2","rcm":"68+2","rdm":"73+2","real_face":"Yes","release_clause_eur":15800000.0,"rf":"62+2","rm":"64+2","rs":"60+2","rw":"62+2","rwb":"70+2","shooting":49.0,"short_name":"C. Chambers","skill_ball_control":74,"skill_curve":55,"skill_dribbling":65,"skill_fk_accuracy":49,"skill_long_passing":70,"skill_moves":2,"st":"60+2","team_jersey_number":21.0,"team_position":"SUB","value_eur":8000000,"value_gbp":"\u00a313.05m","wage_eur":49000,"weak_foot":3,"weight_kg":73,"work_rate":"Low/High"},{"age":24,"attacking_crossing":18,"attacking_finishing":16,"attacking_heading_accuracy":16,"attacking_short_passing":27,"attacking_volleys":16,"body_type":"Lean","club":"Arsenal","contract_valid_until":2020.0,"defending_marking":11,"defending_sliding_tackle":14,"defending_standing_tackle":11,"dob":"1994-09-09","gk_diving":63.0,"gk_handling":66.0,"gk_kicking":67.0,"gk_positioning":64.0,"gk_reflexes":68.0,"gk_speed":39.0,"goalkeeping_diving":63,"goalkeeping_handling":66,"goalkeeping_kicking":67,"goalkeeping_positioning":64,"goalkeeping_reflexes":68,"height_cm":198,"international_reputation":1,"joined":"2013-10-23","long_name":"Matt Macey","mentality_aggression":25,"mentality_composure":52,"mentality_interceptions":15,"mentality_penalties":22,"mentality_positioning":12,"mentality_vision":36,"movement_acceleration":38,"movement_agility":37,"movement_balance":33,"movement_reactions":59,"movement_sprint_speed":40,"nationality":"England","overall":66,"player_positions":"GK","player_url":"https://sofifa.com/player/213407/matt-macey/20/159586","potential":72,"power_jumping":52,"power_long_shots":16,"power_shot_power":50,"power_stamina":33,"power_strength":67,"preferred_foot":"Right","real_face":"No","release_clause_eur":1400000.0,"short_name":"M. Macey","skill_ball_control":19,"skill_curve":16,"skill_dribbling":16,"skill_fk_accuracy":17,"skill_long_passing":24,"skill_moves":1,"team_jersey_number":33.0,"team_position":"RES","value_eur":675000,"value_gbp":"\u00a3225k","wage_eur":12000,"weak_foot":2,"weight_kg":81,"work_rate":"Medium/Medium"}]
         
        if (this.props.players != null) {
            var playersLength = this.props.players.length;
            switch(this.props.slots) {
                case 4:
                    slots.push(<DepthChartSlot players={this.props.players.slice(0,playersLength/4)}/>);
                    slots.push(<DepthChartSlot players={this.props.players.slice(playersLength/4, 2*playersLength/4)}/>);
                    slots.push(<DepthChartSlot players={this.props.players.slice(2*playersLength/4, 3*playersLength/4)}/>);
                    slots.push(<DepthChartSlot players={this.props.players.slice(3*playersLength/4, 4*playersLength/4)}/>);
                    break;
                case 3:
                    slots.push(<DepthChartSlot players={this.props.players.slice(0,playersLength/3)}/>);
                    slots.push(<DepthChartSlot players={this.props.players.slice(playersLength/3, 2*playersLength/3)}/>);
                    slots.push(<DepthChartSlot players={this.props.players.slice(2*playersLength/3, 3*playersLength/3)}/>);
                    break;
                case 2:
                    slots.push(<DepthChartSlot players={this.props.players.slice(0,playersLength/2)}/>);
                    slots.push(<DepthChartSlot playeres={this.props.players.slice(playersLength/2,playersLength)}/>);
                    break;
                default:
                    slots.push(<DepthChartSlot players={this.props.players}/>)    
            }
        }
        
        return (
            <div className="depthChartRow">
                <ul>
                    {slots}
                </ul>
            </div>
        )
    }
}

export default DepthChartRow;