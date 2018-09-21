$( document ).ready(function() {
	var add_post_input = $(".home .add_post_form .add_post_input");
	var add_post_form = $(".home .add_post_form");
	var add_post_div = $(".home .add_post");

	var like_button = $(".home .block_post .like");

	var tweet_counter = $("#tweet_counter");

	add_post_input.keypress(function (e) {
        var code = (e.keyCode ? e.keyCode : e.which);
        if (code == 13) {
            add_post_form.submit();
            return true;
        }
    });

	add_post_form.submit( function( e ) {
		var url;
		var div;

		e.preventDefault();
		call_ajax = $.post(add_post_form.attr( "action" ), add_post_form.serialize());

		call_ajax.done( function ( data ) {
			if (data["success"])
			{
				div = '<div class="block_post">';
				div += '	<div class="user-logo">' + window.user_initials + '</div>';
				div += '	<div class="block_text">';
				div += '		<div class="username">' + window.username + '</div>';
				div += '		<div class="post">' + add_post_input.val() + '</div>';
				div += '		<div class="actions">';
				div += '			<div data-href="'+ window.like_url + data.post_id + '" class="like"><div class="icon_not_like" alt="Like">0</div></div>';
				div += '			<div data-href="" class="icon_comment"><i class="fa fa-comment-o" alt="Show posts"></i></div>';
				div += '		</div>';
				div += '	</div>';
				div += '</div>';

				add_post_div.after(div);
				add_post_input.val("");
				like_button = $(".home .block_post .like");
				like_button.first().click(like_click);
				tweet_counter.text(data.tweet_counter)
			}

		});
	});

	like_button.click(like_click);

	function like_click () {
		var clicked_button = $(this);
		var icon;

		$.get(clicked_button.data("href")).done( function ( data ) {
			if (data["success"])
			{
				icon = clicked_button.children().first();
				if (data["like"])
				{
					icon.toggleClass("icon_not_like icon_like");
					icon.text(data.like_counter);

				}
				else
				{
					icon.toggleClass("icon_not_like icon_like");
					icon.text(data.like_counter);
				}
			}
		});
	}

});
