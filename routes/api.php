<?php

use App\Http\Controllers\Api\V1\CompleteTaskControler;
use App\Http\Controllers\Api\V1\TaskController;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "api" middleware group. Make something great!
|
*/

//Route::apiResource('/V1/tasks',TaskController::class );

Route::prefix('V1')->group(function(){
    Route::apiResource('/tasks',TaskController::class );
    Route::patch('/task/{task}/compleate',CompleteTaskControler::class);
});

Route::middleware('auth:sanctum')->get('/user', function (Request $request) {
    return $request->user();
});
