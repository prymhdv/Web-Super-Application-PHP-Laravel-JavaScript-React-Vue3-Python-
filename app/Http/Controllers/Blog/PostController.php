<?php

namespace App\Http\Controllers\Blog;
use App\Http\Controllers\Controller;
use App\Models\Blog\Like;
use App\Models\Blog\Post;
use App\Models\Blog\Tag;
 
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Gate;

class PostController extends Controller
{
    public function Blog()
    {   $posts = Post::orderBy('created_at', 'desc')->paginate(1); 
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
         
        return view('blog.admin.index', ['posts' => $posts]);
    }

    public function Post($id)
    {
        $post = Post::where('id', $id)->with('likes')->first();
        return view('blog.blog.post', ['post' => $post]);
    }

    public function LikePost($id)
    {
        $post = Post::where('id', $id)->first();
        $like = new Like();
        $post->likes()->save($like);
        return redirect()->back();
    }

    public function CreateTag()
    {
        $tags = Tag::all();
        return view('blog.admin.create', ['tags' => $tags]);
    }

    public function Edit($id)
    {    // if(!Auth::check()){return redirect()->back();  }
        $post = Post::find($id);
        if(Gate::denies('manipulate-post',$post))  
        {
            return redirect()->back();
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
            'content' => $request->input('content')
        ]);
        //$post->save();
        $user->posts()->save($post);
        $post->tags()->attach($request->input('tags') === null ? [] : $request->input('tags'));

        return redirect()->route('Blog.User.index.Route')->with('info', 'Post created, Title is: ' . $request->input('title'));
    }

    public function Update(Request $request)
    {    // if(!Auth::check()){return redirect()->back();  }
        $this->validate($request, [
            'title' => 'required|min:5',
            'content' => 'required|min:10'
        ]);
        $post = Post::find($request->input('id'));
        if(Gate::denies('manipulate-post',$post))  
        {
            return redirect()->back();
        }
        $post->title = $request->input('title');
        $post->content = $request->input('content');
        $post->save();
//        $post->tags()->detach();
//        $post->tags()->attach($request->input('tags') === null ? [] : $request->input('tags'));
        $post->tags()->sync($request->input('tags') === null ? [] : $request->input('tags'));
        return redirect()->route('blog.admin.index')->with('info', 'Post edited, new Title is: ' . $request->input('title'));
    }

    public function Delete($id)
    {
        $post = Post::find($id);
        if(Gate::denies('manipulate-post',$post))  
        {
            return redirect()->back();
        }
        $post->likes()->delete();
        $post->tags()->detach();
        $post->delete();
        return redirect()->route('Blog.User.index.index')->with('info', 'Post deleted!');
    }
}
