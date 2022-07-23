const Twilio=require("twilio");
const client= new Twilio("AC74319e794ee429aa7104381c0f74397f","882e5530386dc3e7fa972e373f289484");

client.messages.list()
.then(messages=>console.log(`most recent message being${messages[0].body}`))
.catch(er=>console.error(er));

console.log('gathering your message');