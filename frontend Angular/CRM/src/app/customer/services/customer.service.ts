import { HttpClient,HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class CustomerService {

  private baseUrl= environment.url;


  constructor(private http:HttpClient) { }

  getallCustomers():Observable<any> {
    return this.http.get(this.baseUrl + "customer/getAll")
  }

  createCustomer(ob:any): Observable<any> {
    let body = JSON.stringify(ob);
    let options = { headers: new HttpHeaders().set('Content-Type', 'application/json') };
    console.log(body);
    return this.http.post<any>(this.baseUrl + "customer/new/" ,ob)
  }

}
