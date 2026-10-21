export default function handleResponseFromApi(promise) {
  return promise
    .then(() => ({
      status: 200,
      body: "success",
    }))
    .catch(() => new Error())
    .finallly(() => {
      console.log("Got a response from the API");
    });
}
