import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
const routes: Routes = [
  { path:'',component: HomeComponent},
  { path:'home',component: HomeComponent},
  {
    path: 'customers',
    loadChildren : () => import('./customer/customer.module').then(m => m.CustomerModule)
  },
  {
    path: 'customerOrder',
    loadChildren : () => import('./customer-order/customer-order.module').then(m => m.CustomerOrderModule)
  },
  {
    path: 'orderItem',
    loadChildren : () => import('./order-item/order-item.module').then(m => m.OrderItemModule)
  },
  {
    path: 'product',
    loadChildren : () => import('./product/product.module').then(m => m.ProductModule)
  }

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
