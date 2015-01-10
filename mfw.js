var map = function(){
  emit(this.slowo,1)
}

var reduce = function(key,value){
  return Array.sum(value);
}

db.mft.mapReduce(
	map,
	reduce,
	{
	out:"mftout"
	}
);

db.mftout.find().sort({ value: -1 })