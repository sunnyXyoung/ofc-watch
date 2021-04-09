
var jsonify = res => res.json();
function ajax(url){
    return new Promise((resolve, reject) => {
        fetch(`./${localStorage.getItem("round")}/${url}`).then(jsonify).then(resolve).catch(reject)
    })
}
function report(url){
    return new Promise((resolve, reject) => {
        fetch(`/ofc/${url}`).then(jsonify).then(resolve).catch(reject)
    })
}
export default {
    getData(url){
        return ajax(url)
    },
    getReport(url){
        return report(url)
    },
}
