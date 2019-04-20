const randomWords = require('random-words');

async function getWords() {
  return Promise.resolve(randomWords().toUpperCase());
}

exports.handler = async function(event, context) {
  try {
    const body = await getWords();
    return { statusCode: 200, body };
  } catch (err) {
    return { statusCode: 500, body: err.toString() };
  }
};
