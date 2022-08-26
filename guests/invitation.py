from email.mime.image import MIMEImage
import os
from datetime import datetime
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.urls import reverse
from django.http import Http404
from django.template.loader import render_to_string
# from guests.models import Party, MEALS

# INVITATION_TEMPLATE = 'guests/email_templates/invitation.html'


# def guess_party_by_invite_id_or_404(invite_id) -> Party:
#     try:
#         return Party.objects.get(invitation_id=invite_id)
#     except Party.DoesNotExist:
#         if settings.DEBUG:
#             # in debug mode allow access by ID
#             return Party.objects.get(id=int(invite_id))
#         else:
#             raise Http404()


# def get_invitation_context(party: Party):
#     preheader_text = 'You are invited!'
#     if party.language == 'da':
#         intro = 'Du' if party.is_singular else 'I'
#         preheader_text = f'{intro} er inviteret'
#     elif party.language == 'vn':
#         # TODO: translate
#         pass

#     return {
#         'title': "Lion's Head",
#         'main_image': 'bride-groom.png',
#         'main_color': '#fff3e8',
#         'font_color': '#666666',
#         'page_title': f'Søren and Thu - {preheader_text}',
#         'preheader_text': preheader_text,
#         'invitation_id': party.invitation_id,
#         'party': party,
#         'meals': MEALS,
#         'language': party.language,
#     }


# def _write_to_file(party: Party, url: str):
#     url = settings.WEDDING_WEBSITE_URL + url
#     filename = party.name + '.txt'
#     path = os.path.join(settings.BASE_DIR, 'invitations', filename)
#     text = f"Hi {party.name}!\n\nSøren and Thu are having a wedding and you're invited! We're trying to keep track of everything online so we set up a website to do this. It also contains more than you'd like to know about the event.\n\nYou can view the invitation and RSVP by visiting {url}"
#     if party.language == 'da':
#         text = f"Hej {party.name}!\n\nThu og jeg har jo som du allerede er bekendt med brullyp i Vietnam senere i år. Vi har derfor sat en hjemmeside op med invitationer til bryllupet samt en masse info.\n\nDu kan se og svare på invitationen her: {url}"
#     elif party.language == 'vn':
#         # TODO: Translate
#         pass

#     with open(path, 'w') as f:
#         f.write(text)


# def send_invitation_email(party: Party, test_only: bool = False, recipients=None):
#     if recipients is None:
#         recipients = party.guest_emails

#     url = reverse('invitation', args=[party.invitation_id])
#     if not recipients:
#         _write_to_file(party, url)
#         print(f'===== WARNING: no valid email addresses found for {party.name}, wrote to file =====')
#         return

#     context = get_invitation_context(party)
#     context['email_mode'] = True
#     context['site_url'] = settings.WEDDING_WEBSITE_URL
#     context['couple'] = settings.BRIDE_AND_GROOM
#     template_html = render_to_string(INVITATION_TEMPLATE, context=context)
#     subject = "You're invited"
#     template_text = "You're invited to {}'s wedding. To view this invitation, visit {}".format(
#         settings.BRIDE_AND_GROOM, url
#     )
#     if party.language == 'da':
#         intro = 'Du' if party.is_singular else 'I'
#         subject = f'{intro} er inviteret'
#         template_text = "{} er inviteret til Søren og Thus bryllup. For at se invitationen, besøg da {}".format(
#             intro, url
#         )
#     elif party.language == 'vn':
#         # TODO: translate
#         pass

#     # https://www.vlent.nl/weblog/2014/01/15/sending-emails-with-embedded-images-in-django/
#     msg = EmailMultiAlternatives(subject, template_text, settings.DEFAULT_WEDDING_FROM_EMAIL, recipients,
#                                  cc=settings.WEDDING_CC_LIST,
#                                  reply_to=[settings.DEFAULT_WEDDING_REPLY_EMAIL])
#     msg.attach_alternative(template_html, "text/html")
#     msg.mixed_subtype = 'related'
#     for filename in (context['main_image'], ):
#         attachment_path = os.path.join(os.path.dirname(__file__), 'static', 'invitation', 'images', filename)
#         with open(attachment_path, "rb") as image_file:
#             msg_img = MIMEImage(image_file.read())
#             msg_img.add_header('Content-ID', '<{}>'.format(filename))
#             msg.attach(msg_img)

#     print('Sending invitation to {} ({})'.format(party.name, ', '.join(recipients)))
#     if not test_only:
#         msg.send()


# def send_all_invitations(test_only: bool, mark_as_sent: bool):
#     to_send_to = Party.in_default_order().filter(is_invited=True, invitation_sent=None).exclude(is_attending=False)
#     for party in to_send_to:
#         send_invitation_email(party, test_only=test_only)
#         if mark_as_sent:
#             party.invitation_sent = datetime.now()
#             party.save()
