<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('users', function (Blueprint $table) {
            $table->id();
            //$table->integer('role_id');
            // $table->unsignedBigInteger('role_id')->nullable()->default(NULL);
            // $table->foreign('role_id')->references('id')->on('roles')->onUpdate('cascade')->onDelete('cascade');
            $table->foreignId('role_id')->constrained()
                ->onDelete('cascade')->onUpdate('cascade');

            $table->timestamps();
            $table->string('name');
            $table->string('email')->unique();
            $table->string('password');
            $table->string('phone');
            $table->text('address');
            $table->string('city');
            $table->string('gender');
            $table->string('ip');
            $table->unique(['email', 'password']);
            $table->rememberToken();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('users');
        //Schema::drop('users');
    }
};
