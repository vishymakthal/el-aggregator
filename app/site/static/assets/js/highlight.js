table = document.getElementById('mainTable');
rows = table.rows;


for(var i=1;i<rows.length;i++){
  if(rows[i].children[2].innerText < 24){
    rows[i].children[2].style.backgroundColor= "#a6bcd3";
  }
}

for(var i=1;i<rows.length;i++){
  potential = rows[i].children[4];
  age = rows[i].children[2].innerText
  if( age <= 25)
  if(potential.innerText >= 85){
    potential.style.backgroundColor= "#408000";
  }
  else if(potential.innerText >= 80){
    potential.style.backgroundColor= "#59b300";
  }
  else if(potential.innerText >= 75){
    potential.style.backgroundColor= "#95c269";
  }
  else if(potential.innerText >= 70){
    potential.style.backgroundColor= "#daffb5";
  }
}
