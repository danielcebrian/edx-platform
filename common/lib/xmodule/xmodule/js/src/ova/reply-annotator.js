/* 
 Reply Annotator Plugin v1.0 (https://github.com/danielcebrian/reply-annotator)
 Copyright (C) 2014 Daniel Cebrian Robles
 License: https://github.com/danielcebrian/reply-annotator/blob/master/License.rst
 
 This program is free software; you can redistribute it and/or
 modify it under the terms of the GNU General Public License
 as published by the Free Software Foundation; either version 2
 of the License, or (at your option) any later version.
 
 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.
 
 You should have received a copy of the GNU General Public License
 along with this program; if not, write to the Free Software
 Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
 */
var _ref,
  __bind = function(fn, me){ return function(){ return fn.apply(me, arguments); }; },
  __hasProp = {}.hasOwnProperty,
  __extends = function(child, parent) { for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor(); child.__super__ = parent.prototype; return child; };

Annotator.Plugin.Reply = (function(_super) {
	__extends(Reply, _super);

	function Reply() {
		this.pluginSubmit = __bind(this.pluginSubmit, this);
		this.updateField = __bind(this.updateField, this);
		_ref = Reply.__super__.constructor.apply(this, arguments);
		return _ref;
	}

	Reply.prototype.field = null;

	Reply.prototype.input = null;

	Reply.prototype.pluginInit = function() {
		console.log("Reply-pluginInit");
		//Check that annotator is working
		if (!Annotator.supported()) {
			return;
		}
		
		//-- Editor
		this.field = this.annotator.editor.addField({
			type: 'input', //options (textarea,input,select,checkbox)
      		load: this.updateField,
			submit: this.pluginSubmit,
		});
		var newfield = Annotator.$('<li class="annotator-item reply-item" style="display:none"><span class="parent-annotation">0</span></li>');//reply-item is the parent value
		Annotator.$(this.field).replaceWith(newfield);
		this.field=newfield[0];
		
		//-- Viewer
		var newview = this.annotator.viewer.addField({
			load: this.updateViewer,
		});

		return this.input = $(this.field).find(':input');
	};
	
	// New JSON for the database
	Reply.prototype.pluginSubmit = function(field, annotation) {
		var replyItem = $(this.annotator.editor.element).find(".reply-item span.parent-annotation"),
			parent = replyItem.html()!=''?replyItem.html():'0';
                console.log(parent);
                console.log(replyItem.html());
		if (parent!='0') annotation.media = 'comment';
		annotation.parent = parent;//set 0, because it is not a reply
		console.log(annotation.parent);
                return annotation.parent;
	};
	

	Reply.prototype.updateViewer = function(field, annotation) {
		var self = this,
			field = $(field),
			ret = field.addClass('reply-viewer-annotator').html(function() {
				var string;
				return self;
			});
		this.annotation = annotation;
		$(field).remove();
		//Create the actions for the buttons
		return ret;
	};
	
	Reply.prototype.updateField = function(field, annotation) {
		//reset parent value
		var replyItem = $(this.annotator.editor.element).find(".reply-item span.parent-annotation");
		return replyItem.html('0');
	};

	return Reply;

})(Annotator.Plugin);

