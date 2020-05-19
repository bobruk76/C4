<template>
  <div class="container">
    <div class="col-sm-10">
      <h1>Задачи</h1>
      <button type="button" id="task-add" class="btn btn-success btn-sm align-left d-block" v-b-modal.todo-modal>Добавить задачу</button>

      <table class="table table-dark table-stripped table-hover">
        <thead class="thead-light">
          <tr>
            <th>Uid</th>
            <th>Описание</th>
            <th>Выполнена?</th>
            <th></th>
          </tr>
        </thead>

        <tbody>
          <tr v-for="(todo, index) in todos" :key="index">
            <td class="todo-uid">{{ todo.uid }}</td>
            <td>{{ todo.description }}</td>
            <td>
              <span v-if="todo.is_completed">Выполнено</span>
              <span v-else>Не выполнено</span>
            </td>
            <td>
              <div class="btn-group" role="group">
                <button type="button" class="btn btn-secondary btn-sm">Обновить</button>
                &nbsp;
                <button type="button" class="btn btn-danger btn-sm">X</button>
              </div>
            </td>
          </tr>
        </tbody>

      </table>

    <b-modal ref="addTodoModal"
            id="todo-modal"
            title="Добавить задачу"
            hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-description-group"
                      label="Описание:"
                      label-for="form-description-input">
            <b-form-input id="form-description-input"
                          type="text"
                          v-model="addTodoForm.description"
                          required
                          placeholder="Завести задачу">
            </b-form-input>
          </b-form-group>
          <b-form-group id="form-complete-group">
            <b-form-checkbox-group v-model="addTodoForm.is_completed" id="form-checks">
              <b-form-checkbox value="true">Задача выполнена?</b-form-checkbox>
            </b-form-checkbox-group>
          </b-form-group>
          <b-button type="submit" variant="primary">Добавить</b-button>
          <b-button type="reset" variant="danger">Сброс</b-button>
      </b-form>
    </b-modal>


    </div>
  </div>
</template>

<style lang="scss" scoped>
  @import "./styles.css";
</style>

<script src="./index.js"></script>