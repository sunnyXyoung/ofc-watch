import store from "./store";
var jsonify = res => res.json();
function ajax(url){
    return new Promise((resolve, reject) => {
      fetch(`./${store.state.round}/${url}`).then(jsonify).then(resolve).catch(reject)
    })
}
export default {
    getData(url){
        return ajax(url)
    }
}
