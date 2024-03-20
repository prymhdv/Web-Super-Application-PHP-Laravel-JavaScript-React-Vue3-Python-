<?php

namespace App\Http\Controllers\Blog;

use App\Http\Controllers\Controller;
use App\Models\Blog\Like;
use App\Models\Blog\Post;
use App\Models\Blog\Tag;
use App\Models\User as User;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Gate;

use Symfony\Component\Process\Process;
use Symfony\Component\Process\Exception\ProcessFailedException;

class PostController extends Controller
{
    public function Blog()
    {
        //$posts = Post::withCount('likes')->orderByDesc('likes_count')->get();
        //dd($posts);
        $posts = Post::withCount('likes')->orderByDesc('likes_count')->orderBy('created_at', 'desc')->paginate(4);//app/config/view.php
        //$posts = Post::orderBy('created_at', 'desc')->get();
        return view('blog.index', ['posts' => $posts]);
        //dd(route('blog.index'));
        //return redirect()->route('blog.index');//page redirected too many times//loop self redirected
    }

    public function Index()
    {
        // if(!Auth::check()){return redirect()->back();  }-->>checked by auth middleware
        //dd('PostController@Index');
        $posts = Post::orderBy('title', 'asc')->get();
        //make one user posts to seeing
        return view('blog.admin.index', ['posts' => $posts]);
    }

    public function Post($id)
    {
        $post = Post::where('id', $id)->with('likes')->first();
        return view('blog.post', ['post' => $post]);
    }

    public function LikePost($id)
    {
        if (1/* IS_Python*/) {
            $process = new Process(['python', 'H:\- Web PHP Laravel\Super Application-OnWork\app\Python\hello.py']);
            $process->run();

            // executes after the command finishes
            if (!$process->isSuccessful()) {
                throw new ProcessFailedException($process);
            }
            //echo $process->getOutput();
            //dd($process->getOutput());
        }
        $post = Post::where('id', $id)->first();
        $like = new Like();
        $post->likes()->save($like);
        return redirect()->back()->with('info', 'Post Liked and RandomArray is:' . $process->getOutput());;
    }

    public function New()
    {
        $tags = Tag::all();
        return view('blog.admin.createForm', ['tags' => $tags]);
    }

    public function Edit($id)
    {    // if(!Auth::check()){return redirect()->back();  }
       $post = Post::find($id);
        if (Gate::denies('manipulate-post', $post)) {
            return redirect()->back()->with('danger', 'Other User Post cant Edited!');;
        }
    
        $tags = Tag::all();
        return view('blog.admin.edit', ['post' => $post, 'postId' => $id, 'tags' => $tags]);
    }

    public function Create(Request $request)
    { // if(!Auth::check()){return redirect()->back();  }
        $this->validate($request, [
            'title' => 'required|min:5',
            'content' => 'required|min:10'
        ]);
        $user = Auth::user();
        //if(!$user)  { return redirect()->back(); }
        $post = new Post([
            'title' => $request->input('title'),
            'content' => $request->input('content'),
            'user_name' => $user->name,
           
        ]);
        //dd($user->name);
        //$post->save();
        $user->posts()->save($post);
        $post->tags()->attach($request->input('tags') === null ? [] : $request->input('tags'));

        return redirect()->route('Blog.User.index.Route')->with('info', 'Post created, Title is: ' . $request->input('title'));
    }

    public function Update($id,Request $request)
    {    // if(!Auth::check()){return redirect()->back();  }
        

        $this->validate($request, [
            'title' => 'required|min:5',
            'content' => 'required|min:10'
        ]);
        $post = Post::find($request->input('id'));
        if (Gate::denies('manipulate-post', $post)) {
            return redirect()->back();
        }
        $post->title = $request->input('title');
        $post->content = $request->input('content');
        $post->save();
        //        $post->tags()->detach();
        //        $post->tags()->attach($request->input('tags') === null ? [] : $request->input('tags'));
        $post->tags()->sync($request->input('tags') === null ? [] : $request->input('tags'));
        
        return redirect()->route('Blog.User.index.Route')->with('warning', 'Post edited, new Title is: ' . $request->input('title'));
    }

    public function Delete($id)
    {
        $post = Post::find($id);
        if (Gate::denies('manipulate-post', $post)) {
            return redirect()->back()->with('danger', 'Other User Post cant Deleted!');;
        }
        $post->likes()->delete();
        $post->tags()->detach();
        $post->delete();
        return redirect()->route('Blog.User.index.Route')->with('info', 'Post Deleted!');
    }
}
