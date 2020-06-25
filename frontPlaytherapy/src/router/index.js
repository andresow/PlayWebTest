import Vue from 'vue';
import Router from 'vue-router';
import CreateDiagnostic from '@/components/Diagnostic/CreateDiagnostic';
import ListDiagnostic from '@/components/Diagnostic/ListDiagnostic';
import CreatePatient from '@/components/Patient/CreatePatient';
import ListPatient from '@/components/Patient/ListPatient';
import UpdatePatient from '@/components/Patient/UpdatePatient';
import CreateTherapist from '@/components/Therapist/CreateTherapist';
import UpdateTherapist from '@/components/Therapist/UpdateTherapist';
import ListTherapist from '@/components/Therapist/ListTherapist';
import CreateFim from '@/components/FIM/CreateFim';
import Home from '@/components/Home/Home';
import InitialInterface from '@/components/InitialInterface/InitialInterface';
import Login from '@/components/Login/Login';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'InitialInterface',
      component: InitialInterface
    },
    {
      path: '/home',
      name: 'Home',
      component: Home
    },
    {
      path: '/diagnostic/create',
      name: 'CreateDiagnostic',
      component: CreateDiagnostic
    },
    {
      path: '/diagnostic',
      name: 'ListDiagnostic',
      component: ListDiagnostic
    },
    {
      path: '/patient/create',
      name: 'CreatePatient',
      component: CreatePatient
    },
    {
      path: '/patient',
      name: 'ListPatient',
      component: ListPatient
    },
    {
      path: '/patient/update',
      name: 'UpdatePatient',
      component: UpdatePatient
    },
    {
      path: '/therapist/create',
      name: 'CreateTherapist',
      component: CreateTherapist
    },
    {
      path: '/therapist/update',
      name: 'UpdateTherapist',
      component: UpdateTherapist
    },
    {
      path: '/therapist',
      name: 'ListTherapist',
      component: ListTherapist
    },
    {
      path: '/FIM/create',
      name: 'CreateFim',
      component: CreateFim
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
  ],
  mode: 'history'
});
