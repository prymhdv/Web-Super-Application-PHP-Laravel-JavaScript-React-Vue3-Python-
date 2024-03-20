<?php

namespace Database\Factories\Blog;

use Illuminate\Database\Eloquent\Factories\Factory;

/**
 * @extends \Illuminate\Database\Eloquent\Factories\Factory<\App\Models\Model>
 */
class PostFactory extends Factory
{
    /**
     * Define the model's default state.
     *
     * @return array<string, mixed>
     */
    public function definition(): array
    {
        return [
            //
            'title'=> fake()->sentence(),
            'content'=>fake()->sentence(),
            //'user_name' => fake()->unique()->text(16),       //  
            'user_name' => fake()->unique()->firstName(),
        ];
        return [];
        //      'first_name' => fake()->unique()->firstName(),
        //     'last_name' => fake()->unique()->lastName(),
        //     'email' => fake()->unique()->word(),
        //     'password' => fake()->unique()->domainName(),
        //     'remember_token' => fake()->unique(true)->numberBetween($min = 1, $max = 999),
    }
}
