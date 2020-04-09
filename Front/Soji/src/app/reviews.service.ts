import { Injectable } from '@angular/core';
import {Review} from './review';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError, map, tap } from 'rxjs/operators';


@Injectable({
  providedIn: 'root'
})
export class ReviewsService {
  private reviewUrl = 'api/reviews';
  constructor( private http: HttpClient) { }
  getReviews(): Observable<Review[]> {
    return this.http.get<Review[]>(this.reviewUrl)
      .pipe(catchError(this.handleError<Review[]>('getHeroes', []))
      );
  }
  private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {

      // TODO: send the error to remote logging infrastructure
      console.error(error); // log to console instead

      // TODO: better job of transforming error for user consumption

      // Let the app keep running by returning an empty result.
      return of(result as T);
    };
  }
}
