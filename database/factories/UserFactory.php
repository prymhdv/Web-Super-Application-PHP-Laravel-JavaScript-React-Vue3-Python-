<?php

namespace Database\Factories;

use Illuminate\Database\Eloquent\Factories\Factory;

/**
 * @extends \Illuminate\Database\Eloquent\Factories\Factory<\App\Models\User>
 */
class UserFactory extends Factory
{
    /**
     * Define the model's default state.
     *
     * @return array<string, mixed>
     */
    public function definition(): array
    {   
        $arrayedUser =  [
                            //
                            'name' => fake()->unique()->text(16),
                            'role_id' =>  '2',
                            'email' => fake()->sentence(),
                            'password' => fake()->sentence(),
                        ];
        
        return $arrayedUser;
    }
}
