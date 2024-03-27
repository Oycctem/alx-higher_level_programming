#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], (_, response, body) => {
  const tasks = JSON.parse(body);
  const completedTasksByUser = {};
  tasks.forEach(task => {
    if (task.completed) {
      completedTasksByUser[task.userId] = (completedTasksByUser[task.userId] || 0) + 1;
    }
  });
  console.log(completedTasksByUser);
});
