import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
const routes: Routes = [
  { path:'',component: HomeComponent},
  { path:'home',component: HomeComponent},
  {
    path: 'customers',
    loadChildren : () => import('./customer/customer.module').then(m => m.CustomerModule)
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }