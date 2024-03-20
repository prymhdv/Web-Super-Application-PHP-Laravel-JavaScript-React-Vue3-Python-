<?php

// @formatter:off
// phpcs:ignoreFile
/**
 * A helper file for your Eloquent Models
 * Copy the phpDocs from this file to the correct Model,
 * And remove them from this file, to prevent double declarations.
 *
 * @author Barry vd. Heuvel <barryvdh@gmail.com>
 */


namespace App\Models{
/**
 * App\Models\Ajax
 *
 * @property int $id
 * @property string $title
 * @property string $description
 * @property \Illuminate\Support\Carbon|null $created_at
 * @property \Illuminate\Support\Carbon|null $updated_at
 * @method static \Illuminate\Database\Eloquent\Builder|Ajax newModelQuery()
 * @method static \Illuminate\Database\Eloquent\Builder|Ajax newQuery()
 * @method static \Illuminate\Database\Eloquent\Builder|Ajax query()
 * @method static \Illuminate\Database\Eloquent\Builder|Ajax whereCreatedAt($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Ajax whereDescription($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Ajax whereId($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Ajax whereTitle($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Ajax whereUpdatedAt($value)
 */
	class Ajax extends \Eloquent {}
}

namespace App\Models\Blog{
/**
 * App\Models\Blog\Comment
 *
 * @property int $id
 * @property \Illuminate\Support\Carbon|null $created_at
 * @property \Illuminate\Support\Carbon|null $updated_at
 * @property string|null $description
 * @property string $type
 * @method static \Illuminate\Database\Eloquent\Builder|Comment newModelQuery()
 * @method static \Illuminate\Database\Eloquent\Builder|Comment newQuery()
 * @method static \Illuminate\Database\Eloquent\Builder|Comment query()
 * @method static \Illuminate\Database\Eloquent\Builder|Comment whereCreatedAt($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Comment whereDescription($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Comment whereId($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Comment whereType($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Comment whereUpdatedAt($value)
 */
	class Comment extends \Eloquent {}
}

namespace App\Models\Blog{
/**
 * App\Models\Blog\Like
 *
 * @property int $id
 * @property \Illuminate\Support\Carbon|null $created_at
 * @property \Illuminate\Support\Carbon|null $updated_at
 * @property int $post_id
 * @property-read \App\Models\Blog\Post|null $post
 * @method static \Illuminate\Database\Eloquent\Builder|Like newModelQuery()
 * @method static \Illuminate\Database\Eloquent\Builder|Like newQuery()
 * @method static \Illuminate\Database\Eloquent\Builder|Like query()
 * @method static \Illuminate\Database\Eloquent\Builder|Like whereCreatedAt($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Like whereId($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Like wherePostId($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Like whereUpdatedAt($value)
 */
	class Like extends \Eloquent {}
}

namespace App\Models\Blog{
/**
 * App\Models\Blog\Link
 *
 * @property \Illuminate\Support\Carbon|null $created_at
 * @property \Illuminate\Support\Carbon|null $updated_at
 * @property int $id
 * @method static \Illuminate\Database\Eloquent\Builder|Link newModelQuery()
 * @method static \Illuminate\Database\Eloquent\Builder|Link newQuery()
 * @method static \Illuminate\Database\Eloquent\Builder|Link query()
 * @method static \Illuminate\Database\Eloquent\Builder|Link whereCreatedAt($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Link whereId($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Link whereUpdatedAt($value)
 */
	class Link extends \Eloquent {}
}

namespace App\Models\Blog{
/**
 * App\Models\Blog\Photo
 *
 * @property int $id
 * @property string $title
 * @property string $src
 * @property string|null $mime_type
 * @property string|null $alt
 * @property string $description
 * @property \Illuminate\Support\Carbon|null $created_at
 * @property \Illuminate\Support\Carbon|null $updated_at
 * @method static \Illuminate\Database\Eloquent\Builder|Photo newModelQuery()
 * @method static \Illuminate\Database\Eloquent\Builder|Photo newQuery()
 * @method static \Illuminate\Database\Eloquent\Builder|Photo query()
 * @method static \Illuminate\Database\Eloquent\Builder|Photo whereAlt($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Photo whereCreatedAt($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Photo whereDescription($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Photo whereId($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Photo whereMimeType($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Photo whereSrc($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Photo whereTitle($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Photo whereUpdatedAt($value)
 */
	class Photo extends \Eloquent {}
}

namespace App\Models\Blog{
/**
 * App\Models\Blog\Post
 *
 * @property int $id
 * @property \Illuminate\Support\Carbon|null $created_at
 * @property \Illuminate\Support\Carbon|null $updated_at
 * @property string $title
 * @property string $content
 * @property int $user_id
 * @property int $post_id
 * @property int $tag_id
 * @property-read \Illuminate\Database\Eloquent\Collection<int, \App\Models\Blog\Comment> $comments
 * @property-read int|null $comments_count
 * @property-read \Illuminate\Database\Eloquent\Collection<int, \App\Models\Blog\Like> $likes
 * @property-read int|null $likes_count
 * @property-read \Illuminate\Database\Eloquent\Collection<int, \App\Models\Blog\Tag> $tags
 * @property-read int|null $tags_count
 * @property-read \App\Models\User|null $user
 * @method static \Database\Factories\Blog\PostFactory factory($count = null, $state = [])
 * @method static \Illuminate\Database\Eloquent\Builder|Post newModelQuery()
 * @method static \Illuminate\Database\Eloquent\Builder|Post newQuery()
 * @method static \Illuminate\Database\Eloquent\Builder|Post query()
 * @method static \Illuminate\Database\Eloquent\Builder|Post whereContent($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Post whereCreatedAt($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Post whereId($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Post wherePostId($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Post whereTagId($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Post whereTitle($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Post whereUpdatedAt($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Post whereUserId($value)
 */
	class Post extends \Eloquent {}
}

namespace App\Models\Blog{
/**
 * App\Models\Blog\Tag
 *
 * @property int $id
 * @property \Illuminate\Support\Carbon|null $created_at
 * @property \Illuminate\Support\Carbon|null $updated_at
 * @property string $name
 * @property string $type
 * @property-read \Illuminate\Database\Eloquent\Collection<int, \App\Models\Blog\Post> $posts
 * @property-read int|null $posts_count
 * @method static \Illuminate\Database\Eloquent\Builder|Tag newModelQuery()
 * @method static \Illuminate\Database\Eloquent\Builder|Tag newQuery()
 * @method static \Illuminate\Database\Eloquent\Builder|Tag query()
 * @method static \Illuminate\Database\Eloquent\Builder|Tag whereCreatedAt($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Tag whereId($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Tag whereName($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Tag whereType($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Tag whereUpdatedAt($value)
 */
	class Tag extends \Eloquent {}
}

namespace App\Models\Hottel{
/**
 * App\Models\Hottel\Client
 *
 * @property int $id
 * @property string $title
 * @property string $name
 * @property string $last_name
 * @property string $address
 * @property string $zip_code
 * @property string $city
 * @property string $state
 * @property string $email
 * @property \Illuminate\Support\Carbon|null $created_at
 * @property \Illuminate\Support\Carbon|null $updated_at
 * @property-read \Illuminate\Database\Eloquent\Collection<int, \App\Models\Hottel\Reservation> $reservations
 * @property-read int|null $reservations_count
 * @method static \Illuminate\Database\Eloquent\Builder|Client newModelQuery()
 * @method static \Illuminate\Database\Eloquent\Builder|Client newQuery()
 * @method static \Illuminate\Database\Eloquent\Builder|Client query()
 * @method static \Illuminate\Database\Eloquent\Builder|Client whereAddress($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Client whereCity($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Client whereCreatedAt($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Client whereEmail($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Client whereId($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Client whereLastName($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Client whereName($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Client whereState($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Client whereTitle($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Client whereUpdatedAt($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Client whereZipCode($value)
 */
	class Client extends \Eloquent {}
}

namespace App\Models\Hottel{
/**
 * App\Models\Hottel\Password
 *
 * @property int $id
 * @property \Illuminate\Support\Carbon|null $created_at
 * @property \Illuminate\Support\Carbon|null $updated_at
 * @property string $password
 * @method static \Illuminate\Database\Eloquent\Builder|Password newModelQuery()
 * @method static \Illuminate\Database\Eloquent\Builder|Password newQuery()
 * @method static \Illuminate\Database\Eloquent\Builder|Password query()
 * @method static \Illuminate\Database\Eloquent\Builder|Password whereCreatedAt($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Password whereId($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Password wherePassword($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Password whereUpdatedAt($value)
 */
	class Password extends \Eloquent {}
}

namespace App\Models\Hottel{
/**
 * App\Models\Hottel\Reservation
 *
 * @property int $id
 * @property string $date_in
 * @property string $date_out
 * @property int $client_id
 * @property int $room_id
 * @property \Illuminate\Support\Carbon|null $created_at
 * @property \Illuminate\Support\Carbon|null $updated_at
 * @property-read \App\Models\Hottel\Client $client
 * @property-read \App\Models\Hottel\Room $room
 * @method static \Illuminate\Database\Eloquent\Builder|Reservation newModelQuery()
 * @method static \Illuminate\Database\Eloquent\Builder|Reservation newQuery()
 * @method static \Illuminate\Database\Eloquent\Builder|Reservation query()
 * @method static \Illuminate\Database\Eloquent\Builder|Reservation whereClientId($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Reservation whereCreatedAt($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Reservation whereDateIn($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Reservation whereDateOut($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Reservation whereId($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Reservation whereRoomId($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Reservation whereUpdatedAt($value)
 */
	class Reservation extends \Eloquent {}
}

namespace App\Models\Hottel{
/**
 * App\Models\Hottel\Room
 *
 * @property int $id
 * @property string $name
 * @property int $floor
 * @property string $description
 * @property \Illuminate\Support\Carbon|null $created_at
 * @property \Illuminate\Support\Carbon|null $updated_at
 * @method static \Illuminate\Database\Eloquent\Builder|Room newModelQuery()
 * @method static \Illuminate\Database\Eloquent\Builder|Room newQuery()
 * @method static \Illuminate\Database\Eloquent\Builder|Room query()
 * @method static \Illuminate\Database\Eloquent\Builder|Room whereCreatedAt($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Room whereDescription($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Room whereFloor($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Room whereId($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Room whereName($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Room whereUpdatedAt($value)
 */
	class Room extends \Eloquent {}
}

namespace App\Models\Hottel{
/**
 * App\Models\Hottel\UserHotel
 *
 * @property-read \Illuminate\Notifications\DatabaseNotificationCollection<int, \Illuminate\Notifications\DatabaseNotification> $notifications
 * @property-read int|null $notifications_count
 * @property-read \Illuminate\Database\Eloquent\Collection<int, \App\Models\Blog\Post> $posts
 * @property-read int|null $posts_count
 * @method static \Illuminate\Database\Eloquent\Builder|UserHotel newModelQuery()
 * @method static \Illuminate\Database\Eloquent\Builder|UserHotel newQuery()
 * @method static \Illuminate\Database\Eloquent\Builder|UserHotel query()
 */
	class UserHotel extends \Eloquent {}
}

namespace App\Models{
/**
 * App\Models\Other
 *
 * @property int $id
 * @property \Illuminate\Support\Carbon|null $created_at
 * @property \Illuminate\Support\Carbon|null $updated_at
 * @property-read \App\Models\Blog\Photo|null $photo
 * @method static \Illuminate\Database\Eloquent\Builder|Other newModelQuery()
 * @method static \Illuminate\Database\Eloquent\Builder|Other newQuery()
 * @method static \Illuminate\Database\Eloquent\Builder|Other query()
 * @method static \Illuminate\Database\Eloquent\Builder|Other whereCreatedAt($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Other whereId($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Other whereUpdatedAt($value)
 */
	class Other extends \Eloquent {}
}

namespace App\Models{
/**
 * App\Models\Password
 *
 * @property int $id
 * @property \Illuminate\Support\Carbon|null $created_at
 * @property \Illuminate\Support\Carbon|null $updated_at
 * @property string $password
 * @method static \Illuminate\Database\Eloquent\Builder|Password newModelQuery()
 * @method static \Illuminate\Database\Eloquent\Builder|Password newQuery()
 * @method static \Illuminate\Database\Eloquent\Builder|Password query()
 * @method static \Illuminate\Database\Eloquent\Builder|Password whereCreatedAt($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Password whereId($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Password wherePassword($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Password whereUpdatedAt($value)
 */
	class Password extends \Eloquent {}
}

namespace App\Models{
/**
 * App\Models\Role
 *
 * @property int $id
 * @property string $name
 * @property \Illuminate\Support\Carbon|null $created_at
 * @property \Illuminate\Support\Carbon|null $updated_at
 * @method static \Database\Factories\RoleFactory factory($count = null, $state = [])
 * @method static \Illuminate\Database\Eloquent\Builder|Role newModelQuery()
 * @method static \Illuminate\Database\Eloquent\Builder|Role newQuery()
 * @method static \Illuminate\Database\Eloquent\Builder|Role query()
 * @method static \Illuminate\Database\Eloquent\Builder|Role whereCreatedAt($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Role whereId($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Role whereName($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Role whereUpdatedAt($value)
 */
	class Role extends \Eloquent {}
}

namespace App\Models{
/**
 * App\Models\Task
 *
 * @property int $id
 * @property string $name
 * @property int $is_completed
 * @property \Illuminate\Support\Carbon|null $created_at
 * @property \Illuminate\Support\Carbon|null $updated_at
 * @method static \Database\Factories\TaskFactory factory($count = null, $state = [])
 * @method static \Illuminate\Database\Eloquent\Builder|Task newModelQuery()
 * @method static \Illuminate\Database\Eloquent\Builder|Task newQuery()
 * @method static \Illuminate\Database\Eloquent\Builder|Task query()
 * @method static \Illuminate\Database\Eloquent\Builder|Task whereCreatedAt($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Task whereId($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Task whereIsCompleted($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Task whereName($value)
 * @method static \Illuminate\Database\Eloquent\Builder|Task whereUpdatedAt($value)
 */
	class Task extends \Eloquent {}
}

namespace App\Models{
/**
 * App\Models\User
 *
 * @property int $id
 * @property int $role_id
 * @property \Illuminate\Support\Carbon|null $created_at
 * @property \Illuminate\Support\Carbon|null $updated_at
 * @property string $name
 * @property string $email
 * @property string $password
 * @property string $phone
 * @property string $address
 * @property string $city
 * @property string $gender
 * @property string $ip
 * @property string|null $remember_token
 * @property-read \Illuminate\Notifications\DatabaseNotificationCollection<int, \Illuminate\Notifications\DatabaseNotification> $notifications
 * @property-read int|null $notifications_count
 * @property-read \Illuminate\Database\Eloquent\Collection<int, \App\Models\Blog\Post> $posts
 * @property-read int|null $posts_count
 * @property-read \App\Models\Role|null $role
 * @method static \Database\Factories\UserFactory factory($count = null, $state = [])
 * @method static \Illuminate\Database\Eloquent\Builder|User newModelQuery()
 * @method static \Illuminate\Database\Eloquent\Builder|User newQuery()
 * @method static \Illuminate\Database\Eloquent\Builder|User query()
 * @method static \Illuminate\Database\Eloquent\Builder|User whereAddress($value)
 * @method static \Illuminate\Database\Eloquent\Builder|User whereCity($value)
 * @method static \Illuminate\Database\Eloquent\Builder|User whereCreatedAt($value)
 * @method static \Illuminate\Database\Eloquent\Builder|User whereEmail($value)
 * @method static \Illuminate\Database\Eloquent\Builder|User whereGender($value)
 * @method static \Illuminate\Database\Eloquent\Builder|User whereId($value)
 * @method static \Illuminate\Database\Eloquent\Builder|User whereIp($value)
 * @method static \Illuminate\Database\Eloquent\Builder|User whereName($value)
 * @method static \Illuminate\Database\Eloquent\Builder|User wherePassword($value)
 * @method static \Illuminate\Database\Eloquent\Builder|User wherePhone($value)
 * @method static \Illuminate\Database\Eloquent\Builder|User whereRememberToken($value)
 * @method static \Illuminate\Database\Eloquent\Builder|User whereRoleId($value)
 * @method static \Illuminate\Database\Eloquent\Builder|User whereUpdatedAt($value)
 */
	class User extends \Eloquent {}
}

namespace App\Models{
/**
 * App\Models\course
 *
 * @property int $id
 * @property \Illuminate\Support\Carbon|null $created_at
 * @property \Illuminate\Support\Carbon|null $updated_at
 * @property string $name
 * @property string|null $description
 * @property int $cost
 * @method static \Illuminate\Database\Eloquent\Builder|course newModelQuery()
 * @method static \Illuminate\Database\Eloquent\Builder|course newQuery()
 * @method static \Illuminate\Database\Eloquent\Builder|course query()
 * @method static \Illuminate\Database\Eloquent\Builder|course whereCost($value)
 * @method static \Illuminate\Database\Eloquent\Builder|course whereCreatedAt($value)
 * @method static \Illuminate\Database\Eloquent\Builder|course whereDescription($value)
 * @method static \Illuminate\Database\Eloquent\Builder|course whereId($value)
 * @method static \Illuminate\Database\Eloquent\Builder|course whereName($value)
 * @method static \Illuminate\Database\Eloquent\Builder|course whereUpdatedAt($value)
 */
	class course extends \Eloquent {}
}

