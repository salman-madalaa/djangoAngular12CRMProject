import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AllComponent } from './all/all.component';
import { NewComponent } from './new/new.component';
import { OrderItemRoutingModule } from './order-item-routing.module';
import { FormsModule } from '@angular/forms';



@NgModule({
  declarations: [
    AllComponent,
    NewComponent
  ],
  imports: [
    CommonModule,
    FormsModule,
    OrderItemRoutingModule
  ]
})
export class OrderItemModule { }
