import { NgModule } from '@angular/core';
import {
  MatButtonModule,
  MatToolbarModule,
  MatInputModule,
  MatSelectModule,
  MatCardModule,
  MatGridListModule,
  MatProgressBarModule,
  MatTableModule,
  MatIconModule,
  MatCheckboxModule
} from '@angular/material';


@NgModule({
  declarations: [],
  imports: [
    MatButtonModule,
    MatToolbarModule,
    MatInputModule,
    MatSelectModule,
    MatCardModule,
    MatGridListModule,
    MatProgressBarModule,
    MatTableModule,
    MatIconModule,
    MatCheckboxModule
  ],
  exports: [
    MatButtonModule,
    MatToolbarModule,
    MatInputModule,
    MatSelectModule,
    MatCardModule,
    MatGridListModule,
    MatProgressBarModule,
    MatTableModule,
    MatIconModule,
    MatCheckboxModule
  ],
})
export class MaterialModule { }
