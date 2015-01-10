var map = function(){
    var alfabetycznie = this.klucz.split("").sort().join("");
    emit(alfabetycznie,{"words":[this.klucz]})
}

var reduce = function(key,value){
    var rezultat = {"words":[]};
    value.forEach(function(word){
    rezultat["words"] = rezultat["words"].concat(word["words"]);
    })
    return rezultat;
}

db.anagram.mapReduce(
	map,
	reduce,
	{out:"wynik"}
);

db.wynik.find()