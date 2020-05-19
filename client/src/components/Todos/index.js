import axios from 'axios';

const todoListURL = 'http://localhost:5000/api/tasks/';
const todoAddURL = 'http://localhost:5000/api/add-task/';

export default {
  name: 'Todo',
  data() {
    return {
      todos: [],
      addTodoForm: {
        description: '',
        is_completed: [],
      }
    };
  },
  methods: {
    getTodos() {
      axios.get(todoListURL)
        .then((response) => {
          this.todos = response.data.tasks;
        });
    },
    resetForm() {
      this.addTodoForm.description = '';
      this.addTodoForm.is_completed = [];
    },
    onSubmit(event) {
      event.preventDefault();
      this.$refs.addTodoModal.hide();
      const requestData = {
        description: this.addTodoForm.description,
        is_completed: this.addTodoForm.is_completed[0],
      };
      console.log(requestData);
      
      axios.post(todoAddURL, requestData)
        .then(() => {
          this.getTodos();
        })
      this.resetForm()
    },
    onReset(event) {
      event.preventDefault();
      this.$refs.addTodoModal.hide();
      this.resetForm();
    },
  },
  created() {
    this.getTodos();
  },
};