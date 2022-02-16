import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class CustomerOrderService {

  private baseUrl= environment.url;


  constructor(private http:HttpClient) { }

  getallCustomerOrders():Observable<any> {
    return this.http.get(this.baseUrl + "customerOrder/getAll")
  }

  createCustomerOrder(ob:any): Observable<any> {
    let body = JSON.stringify(ob);
    let options = { headers: new HttpHeaders().set('Content-Type', 'application/json') };
    console.log(body);
    return this.http.post<any>(this.baseUrl + "customerOrder/new/",ob)
  }

  update(ob:any,id:number):Observable<any>{
    let body = JSON.stringify(ob);
    let options = { headers: new HttpHeaders().set('Content-Type', 'application/json') };
    console.log(body);
    return this.http.post<any>(this.baseUrl + "customerOrder/update/"+id,ob)
  }

  delete(id:number):Observable<any>{
    return this.http.delete(this.baseUrl + 'customerOrder/delete/'+id)
  }
}
